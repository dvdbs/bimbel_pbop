pelajar ='''CREATE TABLE IF NOT EXISTS Pelajar(
   Id_pelajar int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Nama varchar(200) NOT NULL,
   Email varchar(200) NOT NULL UNIQUE,
   Nomor varchar(30) NOT NULL UNIQUE,
   Jenjang_pendidikan ENUM('SD', 'SMP', 'SMA') NOT NULL,
   Jenis_kelamin ENUM('Laki-laki', 'Perempuan') NOT NULL,
   Password varchar(200) not null
    );
'''

pengajar ='''CREATE TABLE IF NOT EXISTS Pengajar(
   Id_pengajar int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Nama varchar(200) NOT NULL,
   Email varchar(200) NOT NULL UNIQUE,
   Nomor varchar(30) NOT NULL UNIQUE,
   Usia varchar(30) NOT NULL,
   Jenis_kelamin ENUM('Laki-laki', 'Perempuan') NOT NULL,
   Password varchar(200) not null
    );
'''

admin = '''CREATE TABLE IF NOT EXISTS Admin(
   Id_admin int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Nama varchar(200) NOT NULL,
   Email varchar(200) NOT NULL UNIQUE,
   Nomor varchar(30) NOT NULL UNIQUE,
   Usia varchar(200) not null,
   Jenis_kelamin ENUM('Laki-laki', 'Perempuan') NOT NULL
    );
'''

def created_table(db) :
    db.create(pelajar)
    db.create(pengajar)
    db.create(admin)
    print("Tabel berhasil dibuat")