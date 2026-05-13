using System.IO.Compression;

class IMobile : ICamera, IMusic
{
    public void TakePhoto()
    {
        Console.WriteLine("Photo clicked");
    }
    public void PlayMusic()
    {
        Console.WriteLine("Music Played");
    }
}