
def clean_my_list(my_list):
    '''
    Puhastab antud nimekirja elementide algusest ja lõpust tühikud ning reavahetused.

    Args:
    my_list(list): Nimekiri, mis sisaldab puhastamata tekstielemente (näiteks faili read koos \n märgiga)

    Returns:
    list: Uus nimekiri, kus kõik elemendid on puhastatud liigsetest tühikustest ja reavahetustest.
    '''
    clean_list=[]
    for element in my_list:
        clean_element=element.strip()
        clean_list.append(clean_element)
    return clean_list
