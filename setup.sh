apt-get install libcurl4-openssl-dev -y
apt-get install libssl-dev -y
apt-get install libjansson-dev -y
apt-get install automake -y
apt-get install autotools-dev -y  
apt-get install build-essential -y
apt-get install nano -y


apt-get install python3 -y
apt-get install python3-distutils -y
apt-get install git -y
git clone https://github.com/thaiboy001/pip
cd pip
python3 get-pip.py
cd ..
python3 -m pip install progress


chmod +x edit-miner
chmod +x run-miner


mv src_run_ccminer ../../etc
mv edit-miner ../../bin
mv run-miner ../../bin


run-miner


cd && cd ../etc/src_run_ccminer/ccminer_mmv
chmod +x build.sh
chmod +x configure.sh
chmod +x autogen.sh
./build.sh

cd && cd ../etc
nano bash.bashrc

run-miner
