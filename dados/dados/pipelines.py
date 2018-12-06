import json

class DadosPipeline(object):

    def open_spider(self, spider):
      self.file = open('dados.txt','w')


    def close_spider(self, spider):
      self.file.close()

    def process_item(self, item, spider):
      line = json.dumps(dict(item)) + '\n'
      self.file.write(line)
      return item