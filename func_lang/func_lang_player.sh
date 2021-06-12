cd
cd func_lang
echo "what is your file called? "
echo " "
read file

cat func_lang.py >> func_lang_temp.py
echo " " > func_lang_temp.py
echo " " >> func_lang_temp.py
echo " " >> func_lang_temp.py
cat programs/$file >> func_lang_temp.py
chmod u+x func_lang_temp.py
./func_lang_temp.py