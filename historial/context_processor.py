def total_historial(request):
    total = 0
    if request.user.is_authenticated:
        if "historial" in request.session.keys():
            for key, value in request.session["historial"].items():
                total += int(value["acumulado"])
    return {"total_historial": total}