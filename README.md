<!DOCTYPE HTML>
<html>
<body>

<h1> Water Contamination Analysis using Hadoop and visualization using sci-kit</h1>
<hr>
<p> I retrieve data of water contamination levels in india over a period of 4 years and use map reduce on it to get desirable knowledge out of it. I then normalize and visualize the data using sci-kit library in python.</p>

<h3>Prerequisites & Software Required</h3>
<p>
<ul style="list-style-type:disc">
    <li>Python</li>
    <li>Scikit Library</li>
    <li>Hadoop Commands</li>
    <li>Jupyter Notebook</li>
    <li>Oracle VM VirtualBox</li>
</ul>
</p>

<h3>Dataset</h3>

<p>The dataset is acquired from the site of data.gov.in which offer real dataset. 
<br>The data consists of 4 years' data i.e.2009-2012. 
<br>The dataset has 8 attributes and is really huge, just the 2009's data has over 1,80,000 rows.
</p>


<h3>Hadoop Commands Used</h3>
<ul style="list-style-type:disc">
    <li>Hadoop fs -put (filename)</li>
        <p>This command puts the file into HDFS. We use it to put our dataset into the cluster.</p>
    <li>Hadoop fs -get (folder/file name)</li>
        <p> This command get the file/folder from hdfs and puts it into your pc. We use this to retrieve the results for further use in JupyterNotebook.</p>
    <li>Hadoop fs -cat (filename)</li>
        <p> This command is used to read the output retrieved after executing map reduce functions.</p>
    <li> hs (mapper filename) (reducer filename) (input filename) (output filename)</li>
        <p> This command is an alias provided by cloudera that is used to execute the map reduce function.</p>
    <li>Hadoop fs -rm (filename)</li>
        <p> This command is used to delete any non-empty folder/ any file in the HDFS.</p>
    <li>Hadoop fs -rmr (foldername)</li>
        <p> This command is used to recursively delete files inside a folder.</p>
</ul>

<h3>Data Achieved:</h3>
<p>After using hadoop map reduce commands I achieve a data which looks like this:</p>
<img src="s.jpg" alt="sample">
</body>
</html>