# p202408booksconvert
e-book conversion workflow

The workflow converts ebooks from unzipped directory structure with .epub extension into a zipped epub file, which can be read by most readers

This is done via combining command line tools:
    
    1. zip to create an archive from the directory
    2. ebook-convert to convert the format into .mobi format
    3. ebook-convert to convert it back to .epub format

The data should be in the project ./data/Books directory, which is on the same level as .src directory with code.

Useful markdown link: 
- [basic syntax](https://www.markdownguide.org/basic-syntax/)
- [extended syntax](https://www.markdownguide.org/extended-syntax/)




correct output:

```
bash-3.2$ ./s101archive.sh
bash-3.2$ ./s101archive.sh
../data/Books
076F0BE27CF8978D521CC1C404647B82.epub
zip -r -q ../data/Books/b1054/076F0BE27CF8978D521CC1C404647B82_book.epub ../data/Books/b1054/076F0BE27CF8978D521CC1C404647B82.epub - done!
rm -rf ../data/Books/b1054/076F0BE27CF8978D521CC1C404647B82.epub - done!
1% Converting input to HTML...
InputFormatPlugin: EPUB Input running
on /Users/bogdan/elisp/proj/p202408booksconvert/data/Books/b1054/076F0BE27CF8978D521CC1C404647B82_book.epub
Traceback (most recent call last):
  File "calibre/ebooks/conversion/plugins/epub_input.py", line 238, in find_opf
FileNotFoundError: [Errno 2] No such file or directory: 'META-INF/container.xml'
Parsing all content...
34% Running transforms on e-book...
Choosing other.ms-coverimage-standard:data/Books/b1054/076F0BE27CF8978D521CC1C404647B82.epub/OEBPS/dick_9781101077696_msr_cvi_r1.jpg as the cover
Merging user specified metadata...
Detecting structure...
Flattening CSS and remapping font sizes...
Source base font size is 9.60000pt
Removing fake margins...
Removing level div_1 left margin of: 3em
Removing page margins specified in the Adobe page template
Cleaning up manifest...
Trimming unused files from manifest...
Trimming 'data/Books/b1054/076F0BE27CF8978D521CC1C404647B82.epub/OEBPS/dick_9781101077696_msr_ppl_r1.jpg' from manifest
Trimming 'data/Books/b1054/076F0BE27CF8978D521CC1C404647B82.epub/OEBPS/dick_9781101077696_msr_cvt_r1.jpg' from manifest
Creating MOBI Output...
67% Running MOBI Output plugin
Serializing resources...
Creating MOBI 6 output
Applying case-transforming CSS...
Rasterizing SVG images...
Converting XHTML to Mobipocket markup...
Serializing markup content...
  Compressing markup content...
Generating MOBI index for a book
MOBI output written to /Users/bogdan/elisp/proj/p202408booksconvert/data/Books/b1054/076F0BE27CF8978D521CC1C404647B82_book.mobi
Output saved to   /Users/bogdan/elisp/proj/p202408booksconvert/data/Books/b1054/076F0BE27CF8978D521CC1C404647B82_book.mobi
ebook-convert ../data/Books/b1054/076F0BE27CF8978D521CC1C404647B82_book.epub ../data/Books/b1054/076F0BE27CF8978D521CC1C404647B82_book.mobi - done!
1% Converting input to HTML...
InputFormatPlugin: MOBI Input running
on /Users/bogdan/elisp/proj/p202408booksconvert/data/Books/b1054/076F0BE27CF8978D521CC1C404647B82_book.mobi
Parsing all content...
Forcing index.html into XHTML namespace
34% Running transforms on e-book...
Merging user specified metadata...
Detecting structure...
Flattening CSS and remapping font sizes...
Source base font size is 12.00000pt
Removing fake margins...
Cleaning up manifest...
Trimming unused files from manifest...
Trimming 'images/00003.jpg' from manifest
Creating EPUB Output...
67% Running EPUB Output plugin
Splitting markup on page breaks and flow limits, if any...
	Looking for large trees in index.html...
	No large trees found
	Split into 67 parts
The cover image has an id != "cover". Renaming to work around bug in Nook Color
EPUB output written to /Users/bogdan/elisp/proj/p202408booksconvert/data/Books/b1054/076F0BE27CF8978D521CC1C404647B82_b.epub
Output saved to   /Users/bogdan/elisp/proj/p202408booksconvert/data/Books/b1054/076F0BE27CF8978D521CC1C404647B82_b.epub
ebook-convert ../data/Books/b1054/076F0BE27CF8978D521CC1C404647B82_book.mobi ../data/Books/b1054/076F0BE27CF8978D521CC1C404647B82_b.epub - done!

Processed book No. 1 ../data/Books/b1054/076F0BE27CF8978D521CC1C404647B82_b.epub

```


