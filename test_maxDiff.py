def test_MaxDiffr():
    from maxDifference import maxFindDiff
    listV = [1,2,3,6,10]
    maxxNum = maxFindDiff(listV)
    assert maxxNum == 4
    findPos = maxFindDiff(listV)
    assert findPos > 0
    listV2 = [1.1,2.2,3.6,8.9]
    maxxNumFloat = maxFindDiff(listV2)
    assert maxxNumFloat == 5.3
test_MaxDiffr()
