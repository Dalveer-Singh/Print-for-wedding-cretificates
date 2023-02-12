import certificatePrint

def test_NormalisedDate():
    date = certificatePrint.getNormalisedDate('2023-02-06')
    excepted = '06 Feb 2023'
    assert date == excepted, "Expected: "+excepted +", received: "+date

def test_getDay():
    day = certificatePrint.getDayy('2023-02-06')
    excepted = "Monday"
    assert day == excepted, "Expected: "+excepted +", received: "+day

def init():
    test_NormalisedDate();    print("test: date passed");
    test_getDay(); print("test: day passed");

if __name__ == "__main__":
    init();