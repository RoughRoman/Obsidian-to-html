# Obsidian Vault to Wiki Converter
### Overview
- This project is a Tkinter GUI program designed to convert an Obsidian vault, a collection of notes in Markdown, into a wiki-style website. The converter generates an index page and ensures working links to other notes within the vault.

### Features
- Tkinter GUI: User-friendly graphical interface for easy interaction.
- Markdown Conversion: No parsing. Just content wrapped in [md-block](https://github.com/LeaVerou/md-block) tags.
- Index Page Generation: Automatically generates an index page for easy navigation.
- Working Links: Ensures that links within the converted notes point to the correct destinations.

### Requirements
- Python 3.x
- Tkinter library (Technically tkinter is packed with python 3.x but some mac or linux systems need to install it separately.)

### How to Use
1. Download or clone this repo.
2. Run the main.py file
3. Select your vault
4. Select a destination folder
5. Done!

### Planned Features
The following features are planned for future releases to enhance the functionality of the Obsidian Vault to Wiki Converter:

1. Custom Styling Options: Allow users to customize the appearance of the generated wiki-style website through style configuration options.
2. Tag Support: Implement support for Obsidian tags, ensuring that they are reflected in the converted wiki and enable better organization.
3. Search Functionality: Integrate a search feature within the generated website to facilitate quick access to specific notes.
4. Batch Conversion: Enable users to convert multiple Obsidian vaults in batch mode, streamlining the process for users with extensive collections.
5. Error Handling / Stability Improvements: Basically always on the TODO list
6. Progress Bar and Status Updates: Implement a progress bar and real-time status updates during the conversion process to keep users informed.
7. Portability improvements: It does work on all platforms but there are some quirks here and there. Mostly internal stuff that end users wont see.
   
### Contributing
- Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated.
