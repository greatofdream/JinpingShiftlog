.PHONY: all
all: shiftlogAdd.txt
hardDrivePath:=/run/media/zhangaq/新加卷/JPData
GoodRunListAdd:=2187
cpMethod:=scp
#rsync -avzh
runcopy: $(GoodRunListAdd:%=run0000%/Jinping_1ton_Phy_)
shiftlogAdd.txt: shiftlog.xlsx
	python shiftXlsToTxt.py -i $^ -o $@ >$@.log 2>&1
#python shiftXlsToTxt.py -o shiftlogAdd.txt -i shiftlog.xlsx -O GoodRunListAdd.txt
runcopy%: run0000%/Jinping_1ton_Phy_
run%/Jinping_1ton_Phy_:
	mkdir -p $(hardDrivePath)/$(dir $@)
	sshpass -p tuhep819 $(cpMethod)  online@192.168.0.92:~/Readout-1ton/Readout/data/$(notdir $@)*_$*_*.root $(hardDrivePath)/$(dir $@)
.DELETE_ON_ERROR:
.SECONDARY:
