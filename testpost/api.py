import json

from django.http import HttpResponse


def test_post(request):
    """
    test
    :param request:
    :return:
    """
    # if request.method == "POST":
    print('-----' * 10)
    f = request.FILES['kingimage']
    with open('testpost/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return http_rep(0, "---success---", None, 0)


def http_rep(code, msg, data, cache_time):
    """
    返回结果json数据
    :param code:
    :param msg:
    :param data:
    :param cache_time:
    :return:
    """
    result_data = {
        'state': code,
        'msg': msg,
        'data': data,
    }
    rep = HttpResponse(json.dumps(result_data))
    rep['Cache-Control'] = ('no-cache' if cache_time <= 0 else ('public, max-age=%d' % cache_time))
    return rep
