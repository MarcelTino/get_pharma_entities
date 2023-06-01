import pandas as pd
data = pd.read_excel(r'Pharma_entity_list.xlsx')

def get_pharma_entities(text):
    global Company_list
    global output
    Company_List = []
    Type_List=[]
    
    Company_List= data["Entity Name"].tolist()
    # Convert each item to lowercase
    for i in range(len(Company_List)):
        Company_List[i] = Company_List[i].lower()
    
    Type_List= data["Type"].tolist()
    # Convert each item to lowercase
    for i in range(len(Type_List)):
        Type_List[i] = Type_List[i].lower()
    
    import re
    import spacy
    nlp = spacy.load("en_core_web_sm")
    
    tokens=[]
    doc = nlp(text)
    for ent in doc.ents:
        tokens.append(ent)
    
    tokens = list(map(str, tokens))
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    
    # tokens = str.join(" ", tokens)
    # tokens = tokens.lower()
    # tokens=tokens.split()
    
    set1 = set(Company_List)
    set2 = set(tokens)
    
    # Get the set of common elements
    common_elements = set1.intersection(set2)
    
    # Convert the set of common elements back to a list
    common_elements_list = list(common_elements)
    
    data["Entity Name"] = data["Entity Name"].apply(str.lower)
    positions = data.loc[data["Entity Name"].isin(common_elements_list), 'Entity Name'].index.values
    
    
    data_copy = pd.read_excel(r'Pharma_entity_list.xlsx',index_col=False)
    data_copy = data_copy[['Entity Name', 'Type']]
    output = data_copy.loc[positions,:]
    output=pd.DataFrame(output)
    output_print = print(output.to_string(index=False))
    return output_print
    