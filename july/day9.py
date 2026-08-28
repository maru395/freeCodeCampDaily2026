def triage_issue(title, labels):
    title = title.lower()
    updated_labels = list(labels)

    if not updated_labels:
        if "error" in title or "bug" in title:
            updated_labels.extend(["bug", "needs triage"])

        if "feature" in title or "add" in title:
            updated_labels.extend(["enhancement", "discussing"])

    elif "needs triage" in updated_labels and (
        "simple" in title or "easy" in title
    ):
        updated_labels.remove("needs triage")
        updated_labels.append("good first issue")

    elif "discussing" in updated_labels and (
        "planned" in title or "next" in title
    ):
        updated_labels.remove("discussing")
        updated_labels.append("on the roadmap")

    elif "needs triage" in updated_labels or "discussing" in updated_labels:
        if "needs triage" in updated_labels:
            updated_labels.remove("needs triage")

        if "discussing" in updated_labels:
            updated_labels.remove("discussing")

        updated_labels.append("help wanted")

    if "security" in title:
        updated_labels.append("critical")

    # Remove duplicate labels while preserving their order.
    return list(dict.fromkeys(updated_labels))
