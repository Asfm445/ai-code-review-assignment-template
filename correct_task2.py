# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.


def count_valid_emails(emails):
    count = 0



    for email in emails:

        if not isinstance(email, str):
            continue
        
        split_email=email.split("@")
        if len(split_email)!=2:
            continue
        local_part, domain_part = split_email
        if not local_part or not domain_part:
            continue
        domain_part_splited=domain_part.split(".")
        if len(domain_part_splited)<2:
            continue
        if any(not part for part in domain_part_splited):
            continue
        count += 1

    return count