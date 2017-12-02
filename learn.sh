trap "exit" INT
echo "Please enter the name of your directory"
read dir
cd /usr/local/lib/python2.7/dist-packages/chatterbot_corpus/data/english/$dir
echo "What do you want name your lesson"?
read lesson
touch /usr/local/lib/python2.7/dist-packages/chatterbot_corpus/data/english/$lesson
echo "New Lesson Created"
echo "Thank You!"
echo "Please enter what you want me to learn"
echo "<space> - - Question"
echo "<space> - Answer"
gedit $lesson.yml

