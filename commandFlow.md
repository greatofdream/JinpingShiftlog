# Record of Jinping Data
## Oxygen, N2
## command flow
### finish the last day data sample
```shell
ps -ef | grep Readout
./endrun.csh
```
### record Warter resistance
+ light
+ dark
### record ultraSonic
+ open software if not opened
+ connect
+ swith off
+ change another connction
+ switch off
### begin new sample
pedestal run
```shell
vim config/config.txt
# Set TriggerMod "0"
./beginrun.csh
./endrun.csh # an file (config/pedestal.txt) will be update
ls -trl
root
[]Pedestal("<runNumber>.root") # this command can be execute in another window
```
new run
```shell
vim config/config.txt
# Set TriggerMod "1"
./beginrun.csh
```
## Go Back

## DetectorSummary
`名称管理器` set variables
such as:
+ DarkR=OFFSET(Data!$I$1,MATCH(MAX(Data!$A:$A)+1,Data!$A:$A)-Plot!$A$2,0,Plot!$A$2)

MATCH(lookup_value, lookup_array, [match_type])
[match](https://support.microsoft.com/zh-cn/office/match-%e5%87%bd%e6%95%b0-e8dffd45-c762-47d6-bf89-533f4a37673a?ui=zh-cn&rs=zh-cn&ad=cn)
[offset](https://support.microsoft.com/zh-cn/office/offset-%E5%87%BD%E6%95%B0-c8de19ae-dd79-4b9b-a14e-b4d906d11b66)
