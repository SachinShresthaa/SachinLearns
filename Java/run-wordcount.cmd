@echo off
setlocal
set HADOOP_HOME=C:\hadoop-3.3.6
set JAVA_HOME=C:\java21
set PATH=%PATH%;%HADOOP_HOME%\bin

cd /d "%~dp0"

if exist wc-classes rmdir /s /q wc-classes
mkdir wc-classes

for /f "delims=" %%c in ('call "%HADOOP_HOME%\bin\hadoop.cmd" classpath') do set HCP=%%c

echo Compiling WordCount.java...
"%JAVA_HOME%\bin\javac.exe" -classpath "%HCP%" -d wc-classes WordCount.java
if errorlevel 1 goto :eof

echo Packaging jar...
"%JAVA_HOME%\bin\jar.exe" -cf wordcount.jar -C wc-classes .

if exist wc-output rmdir /s /q wc-output

echo Running WordCount...
call "%HADOOP_HOME%\bin\hadoop.cmd" jar wordcount.jar WordCount wc-input wc-output

echo.
echo === Output ===
type wc-output\part-r-00000
