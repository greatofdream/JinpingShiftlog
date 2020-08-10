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