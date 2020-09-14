.PHONY: extend split
target:=$(wildcard run????)
extend: $(target:run%=run0000%)

run0000%: run%
        echo $@
        ln -s $^ $@

splitTarget:=$(wildcard run2092-2103/Jinping_1ton_Phy_20??????_0000????.root)

split: $(splitTarget:run2092-2103/Jinping_1ton_Phy_20191230_%.root=%)

#0000%: run2092-2103/Jinping_1ton_Phy_20??????_0000????*.root
0000%: 
        mkdir -p run$@
        rm run$@/*
        for root in $(wildcard run2092-2103/Jinping_1ton_Phy_20??????_0000$**.root);do echo $${root};ln -s $$(pwd)/$${root} run$@/$$(basename $${root}); done
DELETE_ON_ERROR:
SECONDARY:
