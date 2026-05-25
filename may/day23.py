def get_open_issues(issues, prs):
    pr_map = {}
    for p in prs:
        p_clean_sorted = "".join(sorted(str(p).replace('0', '')))
        if p_clean_sorted not in pr_map:
            pr_map[p_clean_sorted] = []
        pr_map[p_clean_sorted].append(p)
        
    open_issues = []
    
    for i in issues:
        i_clean_sorted = "".join(sorted(str(i).replace('0', '')))
        
        if i_clean_sorted in pr_map:
            is_addressed = any(i != p for p in pr_map[i_clean_sorted])
            
            if is_addressed:
                continue 
                
        open_issues.append(i)
        
    return open_issues
