def search_ldap_user(input_uid):
    search_filter = "(|(uid=" + input_uid + "))"
    return ldap_search(search_filter)
