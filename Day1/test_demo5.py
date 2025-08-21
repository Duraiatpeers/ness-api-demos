import pytest


@pytest.mark.order(2)
@pytest.mark.parametrize('status,statuscode',[('Not Found',404),('Success',200),('Internal Server Error',500)])
def test_http_statuses(status,statuscode):
    if(status == 'Not Found'):
        assert statuscode == 404
    elif(status == 'Success'):
        assert statuscode == 200
    elif (status == 'Internal Server Error'):
        assert statuscode == 500



@pytest.mark.order(1)
@pytest.mark.parametrize('browser',[('Chrome'),('Edge'),('Firefox')])
@pytest.mark.parametrize('type',[('normal'),('headless')])
def test_browser_combo(browser,type):
    if (browser == 'Chrome' and type == 'normal'):
        assert True
    elif (browser == 'Edge' and type == 'normal'):
        assert True
    elif (browser == 'Firefox' and type == 'normal'):
        assert True

    if(browser == 'Chrome' and type == 'headless'):
        print('Chrome browser in headless mode')
        assert  True
    elif(browser == 'Edge' and type == 'headless'):
        assert False
    elif (browser == 'Firefox' and type == 'headless'):
        assert False



