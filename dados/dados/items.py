# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class NoticiasItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    author = Field()
    text = Field()
    link = Field()
#VEÍCULOS	MARCA	MODELO	PLACA	COR	LOCAL	DATA E HORA
class StackItem(Item):
    veiculos = Field()
    marca = Field()
    modelo = Field()
    placa = Field()
    cor = Field()
    local = Field()
    data_hora = Field()