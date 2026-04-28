def verify_age(age_str):
    age_str = int(age_str)
    access = "Access Granted" if age_str >= 18 else "Access Denied"

    return access

