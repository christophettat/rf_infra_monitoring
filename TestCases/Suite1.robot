***Settings***
Library 	OperatingSystem

*** Test Cases ***
My Test 1
	Log		test should starts as flag.txt is present on disk
	Remove File  flag.txt
	Log		unstable flag should have been added to the tests results	

