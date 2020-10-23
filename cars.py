import json

car_dict = json.load(open)


# PDF SECTION

most_revenue = "The {car_model} generated the most revenue: {revenue}".format(car_model=temp1, revenue=temp2)
most_sales = "The {car_model} had the most sales: {total_sales}".format(car_model=temp1, total_sales=temp2)
most_popular_year = "The most popular year was {year} with {total_sales} sales.".format(year=temp1,total_sales=temp2)

pdf_body = "{}<br/>{}<br/>{}".format(most_revenue, most_sales, most_popular_year)

reports.generate('/tmp/cars.pdf', 'Sales summary for last month', pdf_body, cars_data)


# EMAIL SECTION

sender = 'automation@example.com'
receiver = '<user>@example.com'
subject = 'Sales summary for last month'
body = "{}\n{}\n{}".format(most_revenue, most_sales, most_popular_year)

message = emails.generate(sender, receiver, subject, body, '/tmp/cars.pdf')
print(message)
#emails.send(message)