
A barcode is a square or rectangular image that can be read by a scanner which consists of a sequence of parallel black lines and white spaces of different widths. Barcodes are used on labels to make them easier to identify. They're used in department stores as part of the buying process, in warehouses to monitor inventory, and on invoices to help with billing, among other things.

................
Barcode History
................
The concept for the barcode was developed by Norman Joseph Woodland, who drew a series of lines in the sand to represent Morse code, and Bernard Silver. A patent was granted in 1966 and NCR became the first company to develop a commercial scanner to read barcode symbology. A pack of Wrigley’s gum was the first item ever scanned, at Marsh’s supermarket in Troy, Ohio, NCR’s hometown.

.................
Business Benefits
.................
Barcodes were developed to improve the speed of sales transactions, but there are other potential benefits to businesses, including: 

1. Better accuracy - Relying on a barcode to process data is far more accurate than relying on manually-entered data, which is prone to errors.
2. Data is immediately available - Because of the processing speed, information about inventory levels or sales is available in real time.
3. Reduced training requirements - Thanks to the simplicity of the barcode scanner, employees need little in the way of training in how to use it. Additionally, thanks to barcodes, there is much less for employees to have to learn and retain.
4. Improved inventory control - Being able to scan and track inventory yields a much more accurate count, as well as a better calculation of inventory turn. Companies can hold less inventory when they know how soon they will need it.
5. Low cost implementation - Generating barcodes is quick and easy, as is installing a barcode system. Potential savings can be realized almost immediately.


.............................
Choosing a Barcode Symbology
.................................
Code 3 of 9 Full ASCII (Also called Code 39) This barcode can be used to store any of the 128 Full ASCII alphanumeric characters, including upper and lower case letters A-Z, numbers 0-9, and punctuation.
Code 3 of 9 Standard (Also called Code 39) Code 39 Standard is the most commonly used barcode. Use Code 39 to store any of the 43 standard alphanumeric characters, including capital letters A-Z, numbers 0-9, and some punctuation.
Code 128 Code 128 is the most easily read barcode and can be used to store any alphanumeric characters. If you are considering using barcodes in your company, Code 128 is a good choice.
Interleave 2 of 5 This barcode can only contain numeric information, and is typically used in industrial and master carton labeling.
Codabar Codabar is often used in libraries and blood banks.
Code 93 Code 93 is similar to Code 39, but allows you to store more characters per inch.
MSI Plessey This barcode can only store numeric information, and is commonly used in warehousing and inventory control.
UPC-A UPC-A is a 12-digit fixed-length barcode. This is the most commonly used barcode in retail product labeling. The first 6 digits are unique to your business, and must be assigned to you by GS1 US.
UPC-E UPC-E is a 6-digit fixed-length barcode. This barcode is a compressed code that is used to mark small packages and paperback books and magazines in retail.
EAN/JAN-13 EAN/JAN-13 can only store 12, 14 or 17 characters. The barcode is similar to UPC-A, but allows you to include the first two digits of a country code.
EAN/JAN-8 EAN/JAN-8 requires the use of 7, 9 or 12 characters. EAN/JAN-8 is similar to the UPC-E, but also allows you to store the first two digits of a country code.
US Postal Code The US Postal Code barcode is also called POSTNET, and is used by the US Postal service for mail delivery.

link http://www.waspbarcode.com/barcode-maker

///////////////////////////////////////////////////////////////////////////////////////////////////////////
A barcode is a square or rectangular image consisting of a series of parallel black lines and white spaces of varying widths. Barcode stores product related data like the date of manufacturing, expiry date, name of the manufacturer, country of the origin and price quantity of the product. There are two types of barcode one is 1D and other is 2D (2 dimensional).

Most of us would have done shopping in malls, shops and like-wise places and at the time of payment at cash counter you must have seen that the salesman had scanned the tag of the product you purchased with barcode reader and you would have been requested to pay the bill.
In this article, you will understand that what is barcode and how is it made?

What is barcode?
Barcode is a machine-readable code in the form of numbers and a pattern of parallel lines of varying widths, printed on a commodity.
Hence a barcode essentially is a way to encode information in a visual pattern that a machine can read. The combination of black and white bars (elements) represents different text characters which follows a set algorithm for that particular barcode.

arcode contains information about a product like; price & weight of the product, date of manufacturing and expiry, name of the manufacturer etc. Barcode is allocated by an international institution set up for this purpose. Every product has a unique barcode all over the world.
There are two types of Barcodes;

1. 1 dimensional or 1D

2. 2 dimensional or 2D (it is known as QR code also)

“1 D” barcode is used in the normal products like groceries, pen, and electronic equipments etc.

“2D” is similar to 1-dimensional barcode, but it can store more data per unit area as compared to the 1D. You must have seen the use of 2D barcode in the Paytm App.

link https://www.jagranjosh.com/general-knowledge/what-is-barcode-and-how-is-it-made-1522059273-1
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
So, now, Let's make a program that reads QR codes and barcodes from a picture. Three packages are needed for this program: OpenCV, NumPy, and pyzbar. The OpenCV and Numpy libraries are well-known among Python programmers. 
OpenCV is a computer vision and machine learning library that is free to use. It's a handy image processing library. This library is being used in our project to process each frame of a video recorded by a computer. Since pyzbar works with OpenCV / numpy ndarrays, we're using Numpy. 

ZBar Bar Code Reader is an open source software suite for reading bar codes from various sources, such as video streams, image files and raw intensity sensors. It supports EAN-13/UPC-A, UPC-E, EAN-8, Code 128, Code 39, Interleaved 2 of 5 and QR Code. These are the Python bindings for the library.

Setting up the environment

1. For OpenCV
pip install opencv-python
...........................
2. For pyzbar
pip install pyzbar

3. For Numpy
pip install numpy


