.PHONY: all
all: shiftlogAdd.txt
hardDrivePath:=.
GoodRunListAdd:=2185 2187 2189 2191

runcopy: $(GoodRunListAdd:%=run0000%/Jinping_1ton_Phy_)
shiftlogAdd.txt: shiftlog.xlsx
	python shiftXlsToTxt.py -i $^ -o $@ >$@.log 2>&1
#python shiftXlsToTxt.py -o shiftlogAdd.txt -i shiftlog.xlsx -O GoodRunListAdd.txt
run%/Jinping_1ton_Phy_:
	mkdir -p $(dir $@)
	cd $(hardDrivePath)/$(dir $@) & rsync -avzh -e 'ssh -p tuhep819' --bwlimit=5000  online@192.168.0.92:~/Readout-1ton/Readout/data/$@*_$*.root $(dir $@)
.DELETE_ON_ERROR:
.SECONDARY:
