holiday_type = input("Enter your preferred holiday type (Beach, Mountain, City): ").strip().lower()

if holiday_type == "beach":
    preference = input("Do you want a relaxing or adventurous beach holiday? ").strip().lower()
    if preference == "relaxing":
        print("Personalized Plan: Spend your day sunbathing on the sand and listening to the waves.")
    elif preference == "adventurous":
        print("Personalized Plan: Book a jet ski rental and try scuba diving in the coral reef.")
    else:
        print("Personalized Plan: Relax by the shoreline with a cold drink.")

elif holiday_type == "mountain":
    season = input("Are you visiting during the summer or winter? ").strip().lower()
    if season == "summer":
        print("Personalized Plan: Pack your gear for an incredible hiking and camping trip up the trails.")
    elif season == "winter":
        print("Personalized Plan: Hit the slopes for an exciting day of skiing and snowboarding.")
    else:
        print("Personalized Plan: Enjoy the breathtaking views from a cozy mountain cabin.")

elif holiday_type == "city":
    focus = input("Are you interested in culture or shopping? ").strip().lower()
    if focus == "culture":
        print("Personalized Plan: Buy a museum pass and take a guided historic walking tour.")
    elif focus == "shopping":
        print("Personalized Plan: Head downtown to explore local boutique shops and open-air markets.")
    else:
        print("Personalized Plan: Explore the downtown architecture and try local street food.")

else:
    print("Invalid choice. A surprise cross-country road trip has been planned for you!")