



currentdir=`pwd`
targetdir="/Users/hongyusu/Codes/chatbot/data/raw/stackexchange/"


cd $targetdir

for filename in ./*7z; do
    7za x $filename
    realname=`echo $filename | sed -e "s/\.\///g" -e "s/\..*//g"`
    rm -rf $realname
    mkdir $realname
    mv *xml $realname
done

cd $currentdir






