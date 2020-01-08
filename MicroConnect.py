from mstrio.microstrategy import Connection


def getAnswer (slot): 
    metric = 0
    metric_PM = 0
    base_url = "https://MICROSTRATEGYSERVER.com/MicroStrategyLibrary/api"
    mstr_username = "MSTR_USER"
    mstr_password = "MSTR_PASSWORD"
    project_name = "Retail (MicroStrategy Tutorial)"
    report_id = "1D6A7D3211E9F763F1300080EFB55B59"
    conn = Connection(base_url, mstr_username, mstr_password, project_name=project_name,
                     login_mode=16)
    conn.connect()


    report_dataframe = conn.get_report(report_id=report_id)
    columns = report_dataframe.columns
    if slot in columns:
        metric = report_dataframe[slot].agg('sum')
        if slot+"_PM" in columns: 
            metric_PM = report_dataframe[slot+"_PM"].agg('sum')
        else:
            print ("Error PM")
    else:
        print ("Error")
    
    return metric, metric_PM


    

if __name__ == '__main__':
    slot = "Revenue"
    print (getAnswer(slot=slot))