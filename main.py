import emailing
import temporary_db
import logging
import json


#Changing the logging default from Warning to Debug 
logging.basicConfig(filename = 'test.log', level=logging.DEBUG)


customers_json = json.loads(temporary_db.customers) #importing the list of customers from temporary.db.py
products_json  = json.loads(temporary_db.products)  #importing the list of products from temporary.db.py

#Displayig the list of customers
for i in customers_json['customers']:
    print("Абонент -->",i['name'], "Идентификатор -->", i['id'])
customer_id = int(input('Выбирите идентификатор абонента: ')) - 1

#exeption if there is no such a customer
try:
    customer_email = customers_json['customers'][customer_id]['email']
except:
    logging.error('there is not susch a customer {}'.format(customer_id+1))
    

#Displauing the list of products
for j in products_json['products']:
    print("Товар -->",j['name'], "Идентификатор -->", j['id'])
product_id = int(input('Выбирите идентификатор товара: ')) - 1

#Generating text for sending 
message_text = 'Задравствуйте ' + customers_json['customers'][customer_id]['name'] + '! \n' + \
               'Ваша покупка ' + products_json['products'][product_id]['name'] + \
               ' на сумму ' + products_json['products'][product_id]['product_price'] + ' сомони.'   

subject_text = 'AlifTest'

logging.debug('customer id: {} product id: {}'.format(customer_id, product_id))
print('сообщение было отравлено')
#Sending message by using function from emailing.py file
if __name__ == '__main__':
   emailing.email_customer(subject_text, message_text, customer_email)

