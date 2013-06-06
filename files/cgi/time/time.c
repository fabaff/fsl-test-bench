/*
* time.c - A simple CGI which displays the system time.
*
* Copyright (c) 2013 Fabian Affolter <fabian@affolter-engineering.ch>
*
* All rights reserved.
* 
* This program is free software; you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation; either version 2 of the License, or
* (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program; if not, write to the Free Software
* Foundation, Inc.,
* 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void print_header(void) {
    printf("Content-Type: text/html\n\n");
}

void print_html_header(char *title) {
    printf("<html>\n<head>\n");
    printf("<title>%s</title>\n", title);
    printf("</head>\n<body>\n");
}

void print_html_heading(char *heading) {
    printf("<h1>%s</h1>\n", heading);
}

void print_content(void) {
    time_t curtime;
    time(&curtime);
    printf("%s", ctime(&curtime));
}

void print_html_footer(void) {
    char date[3] = "now";
    printf("<center><small>&copy; <a href='https://fedorahosted.org/security-spin/'>Fedora Security Lab</a> 2013 - Page generated %s</small></center>", date);
}

void print_html_end(void) {
    printf("\n</body>\n</html>\n");
}


int main(void) {
    print_header();
    print_html_header("Information delivered by CGI (C)");
    print_html_heading("Date and Time");
    print_content();
    print_html_footer();
    print_html_end();
    return EXIT_SUCCESS;
}
