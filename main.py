cd Desktop/
bash anuka

1. დაწერეთ სკრიფტი რომელიც მომხმარებელს მოთხოვს შეიყვანოს სახელი და გვარი ასევე ჯგუფი. დამატებით
მოითხოვოს შეიტანო ოთხი რიცხვი და დააბრუნებს ამ 4 რიცხვის ჯამს, ნამრავსაშუალო არითმეტიკულს, ასევე
პირველი და მესამე რიცხვცს ჯამს გასამკეცებულს.

#!/bin/bash
read -p "sheiyvane saxeli, gvari da jgufis nomeri: " saxeli gvari jgufi
read -p "sheiyvane 4 ricxvi: " a b c d
echo "jami: $(($a+$b+$c+$d))"
echo "namravli: $(($a*$b*$c*$d))"
echo "sahualo: $[$(($a+$b+$c+$d))/4]"
echo "gasamkecebuli: $[$(($a+$c))]"

2. დაწერე სკრიპტი რომელიც გამოიყენებს შენ შექმნილ ფუნქცია quiz6_გვარი რომელიც აბრუნებს სტრქოქონს
BTU-s studenti შენი სახელი გვარი, ასევე მიმდინარე თარიღის ინფოს. ამავე სქკრიფტში ეს ფუნქცია იქნება
გამოძახებული ციკლით 23-ჯერ.

#!/bin/bash
quiz6_Somkhishvili() {
echo BTU-s studenti Ekaterine Somkhishvili $(date +"%Y -%m-%d")
}
for i in {1..30}
do
quiz6_Somkhishvili
done

3. დაწერეთ სკრიფტი რომელის მომხმარებელს აარჩვინებს (მენიუ) ერთ-ერთ ქომანდს. ეს ქომანდებია:
1 - ვინ იყო სისტემაში შესული; 2 - ამოკითხული ტექსის ტრანსფორმაცია; 3 - გაამოაქვს ოპერატიული
მეხსიერების მდგომარეობა; 4 - გამოაქვს მიმდინარე თვის კალენდარი; 5 - გამოიტანს დისკის დანაყოფების
შესახებ ინფორმმაციას; 6 - ყოფს დიდ ფაილს სასურველ ზომებად; 7 -კონკრეტული დომეინის უკან მყოფი
აიპის გამომტანი; 8 - საბაზისო კალკულატორი; 9 - ფაილის ტიპობრიობა; 10 -რიცხვითი მიმდევრობის შექმნა;
11 - პროცესის პრიორიტეტის შეცვლა; 12 - მფლობელის შეცვლა; სკრიპტს არჩევანი გაკეთების შემდგომ გამოაქვს
სტრიქონი studento sheni სახალი და გვარი airchie და ბრძანების სახელი.

#!/bin/bash
select comm in last tr free cal fdisk split nslookup bc file seq renice chown
do
echo "studento Ekaterine Somkhishvilo shen airchie $comm"
break
done

4. დაწერე სკრიპტი, რომელიც გაშვებისას მოითხოვს 4 ცვლადის მნიშვნელობის შეყვანას - სახელი, გვარი,
ჯგუფის ნომერი, დაბადების ადგილი (ქალაქი). შეყვანის შემდეგ გამოიტანს დაფორმატირებულ შემდეგ ტექსტს
"mogesalmeba universiteti BTU (სიტყვა BTU იტალიკი მწვანე შრიფტით თეთრი ფონით) shen imyofebi" \
" BTU-s studentta momsaxurebis portalshi (ეს სტრიქონი წითელი ხაზგასმული შრიფტით ცისფერ ფონზე)" \
" sheyanili monacemebis analiziT dadgenilia sheni gvaria გვარი (ბაცი ყვითელი შრიფტი) sheni saxelia " \
"სახელი (შავი სტანდარტული შრიფტი) shen iricxebi jgufshi ჯგუფის ნომერი (ციმციმა წითელი შრიფტი) " \
"damatebit dadgenil iqna rom xar დაბადების ადგილი (ქალაქი) (ქალაქის ან დაბის დასახელება იყოს ბოლდი" \
" მწვანე ყვითელ ფონზე ციმციმა)-dan“. გამოსული ტექსტის ბოლოს ჩანდეს ასევე მიმდინარე თარიღი.

#!/bin/bash
read -p "saxeli, gvari, jgufis nomeri, dabadebis adgili: " saxeli gvari jgufi dabadebisadgili
echo -e "mogesalmeba universiteti \e[3;32;107mBTU\e[0m"
echo -e "\e[4;31;106mshen imyofebi BTU-s studentta momsaxurebis portalshi\e[0m"
echo -e "sheyvanili monacemebis analizit dadgenilia sheni gvaria \e[2;33$gvari\e[0m"
echo -e "sheni saxelia $saxeli"
echo -e "shen iricxebi jgufshi \e[5;31m$jgufi\e[0m"
echo -e "damatebit dadgenili iqna rom xar \e[1;32;43m$dabadebisadgili\e[0m -dan"

5. დაწერეთ სკრიპტი რომელსაც ექნება 5 ოფცია d, f, h, j და g. აქედან g ოფციას სჭირდება არგუმენტი
სტრქონული ტიპის შენი გვარი. d ოფციას გამოქონდეს სწისტემის დატვირთულობაზე ინფორმაცია. f ოფციას
გამოქონდეს თუ ვინ იყო წარსულში დალოგინებული. H ოფციას გამოქონდეს fortun-ის შემთხვევითი ტექსტი
შეფერადებული. j ოფციას სქრინსეივერი მატარებელი რომელიც CTRL+C-თი მოკვდავია.  g ოფციას დართული
არგუმენტიტისთვის გამოჰქონდეს სტრიქონი shen xar btu-eli da sheni gvaria და არგუმენტის გადაცემული მნიშვნელობა.

#!/bin/bash
while getopts "dfhjg:" option
do
case $option in
d)
uptime
f)
last
;;
h)
fortune | locate
;;
j)
sl -e
;;
g)
echo shen xar btu-eli da sheni gvaria %OPTARG
;;
esac
done













