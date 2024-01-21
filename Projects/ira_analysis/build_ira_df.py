import xml.etree.ElementTree as ET
import pandas as pd
import os
import pdb
import argparse



def individual_info(indvl):
    """
    A function that builds a dictionary profile of information for individuals,
    including personal information and current employment

    Args:
        - indvl: an XML tree with root = 'Indvl'
    
    Returns:
        - Dictionary with indivudal profile info
    """
    d = {}
    info_keys = ['firstNm','lastNm','midNm','indvlPK']
    org_keys = ['orgNm','orgPK','city','state','cntry']

    info = indvl.findall('./Info')[0]
    orgs = indvl.findall('./CrntEmps/CrntEmp')
    current_emp  = orgs[0]

    for info_key in info_keys:
        try:
            d[info_key] =  info.attrib[info_key]
        except:
            pass
    
    for org_key in org_keys:
        try:
            d[org_key] = current_emp.get(org_key)
        except:
            pass

    d['n_orgs'] = len(orgs)

    return d


def individual_drps(indvl):
    """
    A function that determines, what, if any, DRPs an individual has

    Args:
        - indvl: an XML tree with root = 'Indvl'
    
    Returns:
        - Integer flag: 0 indicates for a given DRP type, flag = 'N', 1 indicates no DRP
        for a given DRP type
    """
    custcomp = indvl.findall("./DRPs/DRP")

    drp_keys = ['hasRegAction','hasCriminal','hasBankrupt','hasCivilJudc','hasBond','hasJudgment','hasInvstgn','hasCustComp','hasTermination']
    
    drp_d = {}

    if not custcomp:
        return drp_d
    else:
        for drp_key in drp_keys:
            if custcomp[0].attrib[drp_key] == "Y":
                drp_d[drp_key] = 1
            else:
                drp_d[drp_key] = 0

    return drp_d


def build_dataframe(xml_file,ind_node='./Indvls/Indvl'):
    """
    A function that constructs a pandas dataframe of individuals

    Args:
        - xml_file: XML file to parse
        - ind_node: Default node to find individuals 
    
    Returns:
        - Pandas dataframe, with each row representing an indiviudal
    """

    # Parse XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    indvls_df = pd.DataFrame()

    # Create list of all Indvl nodes
    indvls = root.findall(ind_node)

    for individual in indvls:
        info = individual_info(individual)
        drps = individual_drps(individual)

        individual_df = pd.DataFrame(info,index=[0])
        
        for drp_type in drps.keys():
            individual_df[drp_type] = drps[drp_type]

        if indvls_df.empty:
            indvls_df = individual_df
        else:
            indvls_df = pd.concat([indvls_df,individual_df],ignore_index=True)
    
    indvls_df.fillna(0,inplace=True)

    return indvls_df


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-rdir","--rootdir", help="Root directory where data can be found",
                    type=str)
    parser.add_argument("-sp","--savepath", help="Directory path where results should be stored",
                    type=str)
    args = parser.parse_args()

    # Final dataframe for results
    df_final = pd.DataFrame()


    # Create list of filepaths for storing
    filepaths = []
    for subdir, dirs, files in os.walk(args.rootdir):
        for file in files:
            if file.endswith(".xml"):
                filepaths.append(args.rootdir+file)

    # Iterate over individual files and append results to final dataframe
    for filepath in filepaths:
        df = build_dataframe(filepath)
        if df_final.empty:
            df_final = df
        else:
            df_final = pd.concat([df_final,df],ignore_index=True)

    if args.savepath:
        name = args.savepath + 'individual_investment_reps_df.csv'
    else:
        name = 'individual_investment_reps_df.csv'
    
    # Save dataframe to csv
    df_final.to_csv(name,index=False)

        







