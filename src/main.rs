use clap::{App, Arg};
use std::collections::HashMap;
use std::fs;
use std::io;
use std::path::{Path, PathBuf};

fn main() -> io::Result<()> {
    let matches = App::new("File Organizer")
        .version("1.0")
        .author("Your Name")
        .about("Organizes files in a directory by extension")
        .arg(
            Arg::with_name("directory")
                .short("d")
                .long("directory")
                .value_name("DIR")
                .help("The directory to organize")
                .default_value(".")
                .takes_value(true),
        )
        .arg(
            Arg::with_name("dry-run")
                .long("dry-run")
                .help("Show what would be done without actually moving files")
                .takes_value(false),
        )
        .get_matches();

    let dir = matches.value_of("directory").unwrap();
    let dry_run = matches.is_present("dry-run");

    println!("Organizing directory: {}", dir);
    if dry_run {
        println!("Dry run mode - no files will be moved");
    }

    organize_directory(dir, dry_run)?;

    Ok(())
}

fn organize_directory(dir: &str, dry_run: bool) -> io::Result<()> {
    let path = Path::new(dir);
    if !path.is_dir() {
        return Err(io::Error::new(
            io::ErrorKind::NotFound,
            "The specified path is not a directory",
        ));
    }

    let mut extension_map: HashMap<String, Vec<PathBuf>> = HashMap::new();

    // Collect files by extension
    for entry in fs::read_dir(path)? {
        let entry = entry?;
        let file_path = entry.path();

        if file_path.is_file() {
            let extension = match file_path.extension() {
                Some(ext) => ext.to_string_lossy().to_lowercase(),
                None => "no_extension".to_string(),
            };

            extension_map
                .entry(extension.to_string())
                .or_insert_with(Vec::new)
                .push(file_path);
        }
    }

    // Move files to appropriate directories
    for (ext, files) in extension_map {
        if files.is_empty() {
            continue;
        }

        let target_dir = path.join(&ext);
        println!("Moving {} files to {}/", files.len(), ext);

        if !dry_run && !target_dir.exists() {
            fs::create_dir(&target_dir)?;
        }

        for file_path in files {
            let file_name = file_path.file_name().unwrap();
            let destination = target_dir.join(file_name);

            println!("  {} -> {}", file_path.display(), destination.display());

            if !dry_run {
                fs::rename(&file_path, &destination)?;
            }
        }
    }

    println!("Organization complete!");
    Ok(())
}
