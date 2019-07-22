
try:
    assert 1==2,'abort..'
    print('Now here')

except AssertionError as errorMsg:
    print('Whoops.', errorMsg)



