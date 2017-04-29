class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write('<html>')
        fout.write('<head>')
        fout.write("<meta charset='utf-8'>")
        fout.write('</head>')
        fout.write('<body>')
        fout.write('<table border="1">')

        for data in self.datas:
            fout.write('<tr>')
            fout.write("<td width='200px'>%s</td>" % data['url'])
            fout.write("<td width='100px'>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()