from lxml import etree

def printall(elements):
    for element in elements:
        print(element.text)

def sum_elements(elements):
    sum = 0
    for element in elements:
        sum += float(element.text)
    return sum

def concat_elements(elements):
    string = ""
    for element in elements:
        string += element.text
    return string

if __name__ == "__main__":
    with open(file="food.xml", mode="r") as f:
        et = etree.parse(f)

        # The price of all foods (as a list)
        printall(et.xpath('food/price'))

        # The sum of all calories
        print(sum_elements(et.xpath('//food/calories')))
        
        # The description of the food with the id: 3
        print(et.xpath('food[3]/description')[0].text) 

        # The price of "French Toast"
        print(et.xpath('food[name="French Toast"]/price')[0].text)

        # The concatenated descriptions of all the "savoury" foods
        print(concat_elements(et.xpath('food[@type="savoury"]/description')))
        
        # The count of ingredients of the food with id: 2
        print(len(et.xpath('food[2]/ingredients/ingredient')))
        
        # The second ingredient of "Homestyle Breakfast"
        print(et.xpath('food[name="Homestyle Breakfast"]/ingredients/ingredient[2]/type')[0].text)
        
        # The count of foods that has "milk" in the ingredients
        print(len(et.xpath('food/ingredients/ingredient[type="milk"]')))

        # The count of ingredients of all "sweet" foods
        print(len(et.xpath("food[@type='sweet']/ingredients/ingredient")))      
