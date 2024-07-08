nepali = {
    'school' : 'विद्यालय',
    'flower' : 'फूल',
    'father' : 'बुबा',
    'mother' : 'आमा',
    'banana' : 'केरा',
    'egg' : 'अण्डा'
}
    

search=input('what do u want to search:').lower()
print(search)
print('the nepali translater of ',search,'is')
print(nepali.get(search))