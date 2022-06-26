

void p(int32_t ag1, int32_t ag2)
{
	puts(ag2);
	void buff;
	read(0, &buff, 0x1000);
	*strchr(&buff, '\n');
	strncpy(ag1, &buff,0x14);
	return;
}

void pp(char *s)
{
	void buff1;
	p(&buff1);
	void buff2;
	p(&buff2);
	strcpy(*s, &buff1);
	*s[strlen(s)] = ' ';
	strcat(*s, &buff2);
	return;
}

int main()
{
	void *s;
	pp(&s);
	puts(&s);
	return 0;
}
