def function (list, num, str1='default'):
    for i in list[:num]:
        print(f'{str1} {i}')


function(['test', 'moretest'], 2, 'goes before')
function(['test', 'moretest'], 2)