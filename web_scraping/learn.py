import requests
import bs4
a = 'https://www.google.com/search?q=anime+op+mc&rlz=1C1UEAD_enCA963CA963&oq=anime+op+mc&aqs=chrome.0.69i59l3j69i57j69i60l4.1485j0j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on'
b = 'https://www.google.com/search?q=anime+enemies+to+lovers&rlz=1C1UEAD_enCA963CA963&ei=BCa3YqjICI2GtQaFir34Bg&ved=0ahUKEwio2tL-8cj4AhUNQ80KHQVFD28Q4dUDCA8&uact=5&oq=anime+enemies+to+lovers&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEcyBAgAEEcyBAgAEEcyBAgAEEcyBAgAEEcyBAgAEEcyBAgAEEcyBAgAEEdKBAhBGABKBAhGGABQlhtYiS1g1C1oAHADeACAAQCIAQCSAQCYAQCgAQHIAQjAAQE&sclient=gws-wiz&safe=active&ssui=on'
for i in range(len(a)):
    if a[i] != b[i]:
        print(a[i], b[i])