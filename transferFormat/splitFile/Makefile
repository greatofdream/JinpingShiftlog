.PHONY: split
inputDir:=2020-9-1
splitTarget:=$(wildcard $(inputDir)/Jinping_1ton_Phy_20??????_0000????.root)

splitNum:=$(splitTarget:$(inputDir)/Jinping_1ton_Phy_%.root=%)
splitN:=$(shell echo $(splitNum)|sed 's/[0-9]*_\B//g' )
#0000%: run2092-2103/Jinping_1ton_Phy_20??????_0000????*.root
split: $(splitN)

#       $(wildcard $(inputDir/Jinping_1ton_Phy_2020$*_%.root=%))
#       echo $@
#       echo $^
0000%: 
        mkdir -p run$@
        #rm run$@/*
        for root in $(wildcard $(inputDir)/Jinping_1ton_Phy_20??????_0000$**.root);do echo $${root};ln -s $$(pwd)/$${root} run$@/$$(basename $${root}); done
DELETE_ON_ERROR:
SECONDARY:
