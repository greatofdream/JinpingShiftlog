.PHONY: all
all: shiftlogAdd.txt
shiftlogAdd.txt: shiftlog.xlsx
	python shiftXlsToTxt.py -i $^ -o $@ >$@.log 2>&1
#python shiftXlsToTxt.py -o shiftlogAdd.txt -i shiftlog.xlsx
.DELETE_ON_ERRORS
.SECONDARY
