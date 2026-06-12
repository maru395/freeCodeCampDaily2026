def analyze_ideas(ideas):
    def get_expected_time(idea):
        name, optimistic, realistic, pessimistic = idea
        
        # PERT Formula: (O + 4*R + P) / 6
        pert_estimate = (optimistic + 4 * realistic + pessimistic) / 6
        
        # Weighted by the length of the idea name
        return pert_estimate * len(name)

    # Sort the ideas array using our calculation function as the sorting key
    ideas.sort(key=get_expected_time)
    
    # Return only the names of the sorted ideas
    return [idea[0] for idea in ideas]
