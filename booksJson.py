import json

bookFile = open('books.json')
bookData = json.load(bookFile)

print('<html><head><title>books</title></head><body>')
print('<table><tr><th>Author</th><th>Title</th><th>Year</th></tr>')

# WRITE CODE HERE

print('</table></body></html>')
