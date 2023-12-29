import csv
import re

old_data_file = "sales_data.csv"
new_data_file = "new_sales_data.csv"
summary_file = "sales_summary_data.csv"
product = set()
productInfo = dict()


def clean_data():
    with open(old_data_file, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        header.append("Year")
        header.append("Month")
        header.append("Category")
        valid_data = [header]
        orderIDP = r"\d+"
        productP = r"Product\s[A-Z]"
        quantityP = r"\d+"
        priceP = r"\d+.\d{2}"
        dateP = r"(\d{4})-(\d{2})-(\d{2})"
        categoryP = r"\[(.+)\](\s.*)"
        for i in reader:
            if all(i):
                matchID = re.search(orderIDP, i[0])
                matchProduct = re.search(productP, i[1])
                matchQuantity = re.search(quantityP, i[2])
                matchPrice = re.search(priceP, i[3])
                matchDate = re.search(dateP, i[4])
                matchCategory = re.search(categoryP, i[5])
                temp = [matchID.group(0),
                        matchProduct.group(0),
                        matchQuantity.group(0),
                        matchPrice.group(0),
                        matchDate.group(0),
                        matchCategory.group(1)+matchCategory.group(2),
                        matchDate.group(1),
                        matchDate.group(2),
                        matchCategory.group(1)]
                valid_data.append(temp)
        with open(new_data_file, "w", newline="") as g:
            writer = csv.writer(g)
            writer.writerows(valid_data)


def analyze_data():
    with open(new_data_file, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for i in reader:
            if i[1] not in product:
                productInfo[i[1]] = {'Quantity': int(i[2]), 'Revenue': float(i[2])*float(i[3])}
                product.add(i[1])
            else:
                productInfo[i[1]]['Quantity'] += int(i[2])
                productInfo[i[1]]['Revenue'] += float(i[2]) * float(i[3])
        sorted_products = sorted(productInfo.items(), key=lambda x: x[1]['Revenue'],reverse=True)
        # print(sorted_products)
        for i in product:
            print(f"{i} have made ${productInfo[i]['Revenue']:.2f}")
            print(f"{productInfo[i]['Quantity']} units of {i} sold")
            print(f"Average revenue made per unit of {i} is {productInfo[i]['Revenue']/productInfo[i]['Quantity']:.2f}")
        highest_product = sorted_products[0][0]
        print(f"{highest_product} has generated the most revenue")
    alphabetical = sorted(productInfo.items(), key=lambda x: x[0])
    with open(summary_file, "w", newline="") as g:
        writer = csv.writer(g)
        header = ['Product', 'Total Sales Revenue', 'Total Quantity Sold', 'Average Price Per Unit']
        writer.writerow(header)
        for item in alphabetical:
            key, value = item
            temp = [
                key,
                round(value['Revenue'],2),
                (value['Quantity']),
                round(value['Revenue'] / value['Quantity'],2)
            ]
            writer.writerow(temp)


clean_data()
analyze_data()
