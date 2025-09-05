import instaloader
from instaloader.__main__ import import_session


def main():
    L = instaloader.Instaloader(
        save_metadata = False,
        # Merge https://github.com/instaloader/instaloader/pull/2578
        download_captions = False
    )

    # L.login("username", "password") does not work since login POST request does not receive sessionid
    # A workaround for missing sessionid (see https://github.com/instaloader/instaloader/issues/2487):
    imported = False
    cont = True
    while not imported and cont:
        try:
            # A browser to import session from ("firefox" | "librewolf" | "safari")
            BROWSER = input("Which browser do you want to import cookies from? ").lower()
            # Merge https://github.com/instaloader/instaloader/pull/2577 (session import fixes)
            # Optionally, merge https://github.com/borisbabic/browser_cookie3/pull/226 (Firefox MSiX support)
            # Optionally, merge https://github.com/borisbabic/browser_cookie3/pull/225 (Firefox via Flatpak support)
            import_session(BROWSER, L)
            imported = True
        except Exception as e:
            print (e)
            cont = input("Do you want to try again? (y/n) ") == "y"
    # If import_session does not work:
    if not imported:
        print("You need to import your session manually then. In your browser, please sign in and provide the following values from Instagram cookies:")
        cont = True
        while cont:
            try:
                username = input("username: ")
                csrftoken = input("csrftoken: ")
                sessionid = input("sessionid: ")
                ds_user_id = input("ds_user_id: ")
                mid = input("mid: ")
                ig_did = input("ig_did: ")
                L.load_session(username, {
                    "csrftoken": csrftoken,
                    "sessionid": sessionid,
                    "ds_user_id": ds_user_id,
                    "mid": mid,
                    "ig_did": ig_did
                })
                L.test_login()
                cont = False
            except Exception as e:
                print(e)
                print("Please try again:")

    LATEST_STAMPS_FILEPATH = input("Please enter a path to a file for storing latest profile timestamps (the file will be created automatically): ")
    INPUT_FILEPATH = input("Please enter a path to an input file containing profile URLS, one in a line (the file must exist): ")
    with open(LATEST_STAMPS_FILEPATH, "a") as latest_stamps_file, open(INPUT_FILEPATH) as input_file:

        stamps = instaloader.LatestStamps(LATEST_STAMPS_FILEPATH)
        
        for line in input_file:
            # Remove leading and trailing " " and "\n" from line:
            line = line.strip(" \n")
            if line:
                if "instagram.com/" not in line:
                    print(f"Incorrect string format: {line}", file=sys.stderr)
                else:
                    username_start = line.find("instagram.com/") + len("instagram.com/")
                    line = line[username_start:]
                    first_slash = line.find("/") if "/" in line else len(line)
                    first_question = line.find("?") if "?" in line else len(line)
                    username = line[:min(first_slash, first_question)]
                    print(f"Working on {username}...")

                    try:
                        profile = instaloader.Profile.from_username(L.context, username)

                        # Merge https://github.com/instaloader/instaloader/pull/2581 (SYSTEMEXITs in case of substantial Instagram requirements)
                        # Optionally, merge https://github.com/instaloader/instaloader/pull/2579 (logging format improvement)
                        L.download_profiles(
                            [profile],
                            profile_pic = False,
                            # posts = True, (default)
                            latest_stamps = stamps,
                            reels = True
                        )
                    except Exception as e:
                        # Treat exceptions as related to the current profile only, and therefore non-critical
                        print(e)

                    # Check if the account is still accessible:
                    L.test_login()


    input("Downloading has been completed! Press Enter to close this window: ")


if __name__ == "__main__":
    main()
